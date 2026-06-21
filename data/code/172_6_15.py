def create_identifier_description_map():
    identifiers = ["id1", "id2", "id3"]
    descriptions = ["desc1", "desc2", "desc3"]
    return dict(zip(identifiers, descriptions))

if __name__ == '__main__':
    identifier_description_map = create_identifier_description_map()
    print(identifier_description_map)