def create_immutable_lookup_table(data: list) -> dict:
    return {frozenset(item): item for item in data}
if __name__ == '__main__':
    sample_data = [[1, 2], [3, 4], [5]]
    lookup_table = create_immutable_lookup_table(sample_data)
    print(lookup_table)