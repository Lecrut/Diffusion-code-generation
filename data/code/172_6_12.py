class IdentifierMapper:
    IDENTIFIERS = ["apple", "banana", "cherry"]
    DESCRIPTIONS = ["fruit", "yellow fruit", "red fruit"]

    @staticmethod
    def map_identifiers_to_descriptions():
        return dict(zip(IdentifierMapper.IDENTIFIERS, IdentifierMapper.DESCRIPTIONS))

if __name__ == '__main__':
    mapper = IdentifierMapper()
    mapped_dict = mapper.map_identifiers_to_descriptions()
    print(mapped_dict)