IDENTIFIERS = ("a", "b", "c", "d")
DESCRIPTIONS = ("apple", "banana", "cherry", "date")

def align_identifiers_with_descriptions():
    return dict(zip(IDENTIFIERS, DESCRIPTIONS))

if __name__ == '__main__':
    aligned_dict = align_identifiers_with_descriptions()
    print(aligned_dict)