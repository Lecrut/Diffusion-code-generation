def create_id_to_description_mapping():
    unique_ids = ["id1", "id2", "id3"]
    descriptions = ["Description 1", "Description 2", "Description 3"]
    return dict(zip(unique_ids, descriptions))

if __name__ == '__main__':
    sample_mapping = create_id_to_description_mapping()
    print(sample_mapping)