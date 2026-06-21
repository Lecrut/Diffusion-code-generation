import spacy

def is_mutually_exclusive(statement1: str, statement2: str) -> bool:

    def get_semantic_representation(stmt: str):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(stmt)
        return [token.text for token in doc]
    if not isinstance(statement1, str) or not isinstance(statement2, str):
        raise ValueError('Both inputs must be strings')
    rep1 = get_semantic_representation(statement1)
    rep2 = get_semantic_representation(statement2)
    return set(rep1).isdisjoint(set(rep2))
if __name__ == '__main__':
    print(is_mutually_exclusive('The sky is blue', 'The grass is green'))
    print(is_mutually_exclusive('The sky is blue', 'The moon is bright'))