identifiers = ['id1', 'id2', 'id3']
descriptions = ['desc1', 'desc2', 'desc3']

def align_identifiers_with_descriptions(ids, descs):
    return dict(zip(ids, descs))

if __name__ == '__main__':
    aligned_dict = align_identifiers_with_descriptions(identifiers, descriptions)
    print(aligned_dict)