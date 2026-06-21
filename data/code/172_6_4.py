identifiers = ['id001', 'id002', 'id003']
descriptions = ['apple', 'banana', 'cherry']

def align_identifiers_with_descriptions(ids, descs):
    return dict(zip(ids, descs))

if __name__ == '__main__':
    aligned_dict = align_identifiers_with_descriptions(identifiers, descriptions)
    print(aligned_dict)