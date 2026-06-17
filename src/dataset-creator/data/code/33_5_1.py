def create_name_set(names):
    return set(name.lower().strip() for name in names)
def check_existence(target_names, existing_set):
    target_lower = {name.lower().strip() for name in target_names}
    def exists_in_database(name):
        if not isinstance(existing_set, (set)):
            raise TypeError("Existing set must be a Python set")
        return any(name.lower().strip() == candidate 
                   for candidate in existing_set)
def main():
    sample_data = ["Alice", "Bob Smith", "CHARLIE", "david"]
    name_database = create_name_set(sample_data)
    test_queries = [
        ("Eve"),
        ("bob smith"),
        ("alice")
    ]
    for query in test_queries:
        result = any(query.lower().strip() == candidate 
                    for candidate in name_database)
        if __name__ == '__main__':
            print(f"Query '{query}': {'Found' if result else 'Not Found'}")
if __name__ == '__main__':
    main()