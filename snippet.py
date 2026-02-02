#!/usr/bin/env python3
"""
Code Snippet Manager with tags and search
"""

import os
import json


class SnippetManager:
    def __init__(self, db_file: str = "snippets.json"):
        self.db_file = db_file
        self.snippets = self.load_snippets()
    
    def load_snippets(self) -> Dict:
        if os.path.exists(self.db_file):
            with open(self.db_file) as f:
                return json.load(f)
        return {}
    
    def save_snippets(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.snippets, f, ensure_ascii=False, indent=2)
    
    def add(self, name: str, code: str, language: str, tags: list):
        snippet_id = len(self.snippets) + 1
        self.snippets[snippet_id] = {
            "name": name,
            "code": code,
            "language": language,
            "tags": tags,
            "created_at": __import__('datetime').datetime.now().isoformat()
        }
        self.save_snippets()
        return snippet_id
    
    def search(self, query: str) -> list:
        query = query.lower()
        results = []
        for sid, s in self.snippets.items():
            if (query in s["name"].lower() or 
                query in s["language"].lower() or 
                any(query in t.lower() for t in s.get("tags", []))):
                results.append(s)
        return results
    
    def list_by_language(self, lang: str) -> list:
        return [s for s in self.snippets.values() if s["language"] == lang]
    
    def run(self):
        print(f"📦 Snippet Manager - {len(self.snippets)} snippets")
        print("Usage: snippet.py add|search|list")


if __name__ == "__main__":
    manager = SnippetManager()
    manager.run()
