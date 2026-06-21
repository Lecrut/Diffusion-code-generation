def align_identifiers_with_descriptions(identifiers, descriptions):
    return dict(zip(identifiers, descriptions))

if __name__ == '__main__':
    sample_identifiers = ["id1", "id2", "id3"]
    sample_descriptions = ["desc1", "desc2", "desc3"]
    aligned_dict = align_identifiers_with_descriptions(sample_identifiers, sample_descriptions)
    print(aligned_dict)