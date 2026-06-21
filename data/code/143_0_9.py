def check_contradiction(statement1: str, statement2: str) -> bool:
    if not isinstance(statement1, str) or not isinstance(statement2, str):
        raise ValueError("Both inputs must be strings.")

    if statement1 == statement2:
        return False

    return 'not' in statement1 and statement1.replace('not', '') in statement2 \
           or 'not' in statement2 and statement2.replace('not', '') in statement1

if __name__ == '__main__':
    print(check_contradiction('The sky is blue.', 'The sky is not blue.'))
    print(check_contradiction('It is raining.', 'It is not raining.'))
    print(check_contradiction('The sun is shining.', 'The sun is not shining.'))
    print(check_contradiction('The moon is full.', 'The moon is not full.'))
    print(check_contradiction('The grass is green.', 'The grass is blue.'))
    print(check_contradiction('It is daytime.', 'It is nighttime.'))