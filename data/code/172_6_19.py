def align_identifiers_with_descriptions(ids, descriptions):
    if len(ids) != len(descriptions):
        raise ValueError("IDs and descriptions must have the same length")
    return dict(zip(ids, descriptions))

if __name__ == '__main__':
    sample_ids = ["a", "b", "c"]
    sample_descriptions = ["apple", "banana", "cherry"]
    aligned_dict = align_identifiers_with_descriptions(sample_ids, sample_descriptions)
    print(aligned_dict)