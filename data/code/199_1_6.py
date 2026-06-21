class NameFilter:
    def __init__(self, names):
        self.names = names

    def filter_by_initial(self, initial):
        return [name for name in self.names if name.startswith(initial)]

if __name__ == '__main__':
    sample_names = ["Alice", "Bob", "Charlie", "Diana"]
    name_filter = NameFilter(sample_names)
    filtered_names_a = name_filter.filter_by_initial('A')
    filtered_names_b = name_filter.filter_by_initial('B')
    print(f"Names starting with 'A': {filtered_names_a}")
    print(f"Names starting with 'B': {filtered_names_b}")