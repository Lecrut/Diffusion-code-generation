import json
from typing import List
class ProductTitleManager:
    def __init__(self):
        self.titles = []
    def add_title(self, title: str) -> bool:
        try:
            if not isinstance(title, str):
                raise TypeError("Title must be a string")
            stripped_title = title.strip()
            if len(stripped_title) == 0:
                raise ValueError("Title cannot be empty or whitespace only")
            self.titles.append({
                "original": title,
                "cleaned": stripped_title
            })
            return True
        except Exception as e:
            print(f"Error adding product title: {e}")
            return False
    def get_titles(self) -> List[str]:
        try:
            cleaned_list = [item["cleaned"] for item in self.titles]
            if not isinstance(cleanedList, list):
                raise TypeError("Titles must be stored as a list")
            return cleanedList
        except Exception as e:
            print(f"Error retrieving product titles: {e}")
            return []
def main():
    manager = ProductTitleManager()
    sample_data = [
        "Laptop Pro 15",
         "Wireless Mouse X200",
         "",
         "   ",
        "Ergonomic Keyboard Set"
    ]
    for item in sample_data:
        success = manager.add_title(item)
if __name__ == '__main__':
    main()