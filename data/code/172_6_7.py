def align_ids_descriptions(ids, descriptions):
    return dict(zip(ids, descriptions))

if __name__ == '__main__':
    sample_ids = ["a", "b", "c"]
    sample_descriptions = ["apple", "banana", "cherry"]
    aligned_dict = align_ids_descriptions(sample_ids, sample_descriptions)
    print(aligned_dict)