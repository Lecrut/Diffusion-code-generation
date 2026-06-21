def align_identifiers_with_descriptions(unique_ids, descriptions):
    return dict(zip(unique_ids, descriptions))

if __name__ == '__main__':
    unique_ids = ["id1", "id2", "id3", "id4"]
    descriptions = ["Apple", "Banana", "Cherry", "Date"]
    aligned_dict = align_identifiers_with_descriptions(unique_ids, descriptions)
    print(aligned_dict)