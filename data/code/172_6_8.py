class IdentifierDescriber:
    IDENTIFIERS = {
        "apple": "a fruit",
        "banana": "a long curved fruit",
        "cherry": "a small round fruit",
        "date": "a sweet fruit"
    }

    @staticmethod
    def get_descriptions():
        return dict(zip(IdentifierDescriber.IDENTIFIERS.keys(), IdentifierDescriber.IDENTIFIERS.values()))

if __name__ == '__main__':
    descriptions = IdentifierDescriber.get_descriptions()
    print(descriptions)