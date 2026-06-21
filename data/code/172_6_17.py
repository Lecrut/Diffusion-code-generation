def create_identifier_map(unique_ids, descriptions):
    if not unique_ids or not descriptions:
        raise ValueError("Both unique_ids and descriptions must be non-empty sequences.")
    
    if len(unique_ids) != len(descriptions):
        raise ValueError("The length of unique_ids and descriptions must match.")

    return dict(zip(unique_ids, descriptions))

if __name__ == '__main__':
    sample_ids = ["id1", "id2", "id3"]
    sample_descriptions = ["apple", "banana", "cherry"]

    identifier_map = create_identifier_map(sample_ids, sample_descriptions)
    print(identifier_map)