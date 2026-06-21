ID_DESCRIPTIONS = {
    "id1": "apple",
    "id2": "banana",
    "id3": "cherry",
    "id4": "date"
}

def align_identifiers_with_descriptions():
    return dict(zip(ID_DESCRIPTIONS.values(), ID_DESCRIPTIONS.keys()))

if __name__ == '__main__':
    aligned_dict = align_identifiers_with_descriptions()
    print(aligned_dict)