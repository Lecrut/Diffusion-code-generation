import sys
class ProductTitleManager:
    def __init__(self):
        self._titles = []
    def add_title(self, title: str) -> bool:
        if not isinstance(title, str):
            raise TypeError("Product title must be a string.")
        if len(title.strip()) == 0:
            raise ValueError("Product title cannot be empty after stripping whitespace.")
        existing = [t for t in self._titles if t.lower() == title.lower()]
        if any(t.title().strip() == title.strip() for t in existing):
            return False
        clean_title = title.strip()
        self._titles.append(clean_title)
        return True
    def get_titles(self) -> list:
        return [t for t in self._titles]
def main():
    manager = ProductTitleManager()
    sample_data = [
        "Laptop Pro 15",
        "",
        None,
        "   Wireless Mouse ",
        "Wireless Mouse",
        12345,
        "Smartphone X"
    ]
    for item in sample_data:
        try:
            result = manager.add_title(item) if item is not None else False
            print(f"Added '{item}' -> {result}")
        except (TypeError, ValueError) as e:
            print(f"Error processing input: {e}", file=sys.stderr)
if __name__ == '__main__':
    main()