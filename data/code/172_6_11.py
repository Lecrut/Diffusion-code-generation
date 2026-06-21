def align_identifiers_with_descriptions(ids, descriptions):
    return dict(zip(ids, descriptions))

if __name__ == '__main__':
    sample_ids = ["id1", "id2", "id3"]
    sample_descriptions = ["description1", "description2", "description3"]
    aligned_dict = align_identifiers_with_descriptions(sample_ids, sample_descriptions)
    print(aligned_dict)