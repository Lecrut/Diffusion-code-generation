def map_identifiers_to_descriptions(ids, descriptions):
    return dict(zip(ids, descriptions))

if __name__ == '__main__':
    sample_ids = ["id1", "id2", "id3"]
    sample_descriptions = ["apple", "banana", "cherry"]
    mapped_data = map_identifiers_to_descriptions(sample_ids, sample_descriptions)
    print(mapped_data)