identifiers = ['id1', 'id2', 'id3']
descriptions = ['apple', 'banana', 'cherry']

def align_identifiers_with_descriptions(ids, descs):
    return dict(zip(ids, descs))

if __name__ == '__main__':
    aligned_data = align_identifiers_with_descriptions(identifiers, descriptions)
    print(aligned_data)