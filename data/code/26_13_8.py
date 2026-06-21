from typing import Any

def get_voter_eligibility(attributes: dict[str, Any]) -> str:
    age = attributes.get('age')
    citizenship = attributes.get('citizenship')
    registered = attributes.get('registered')

    if not isinstance(age, (int, float)):
        return 'invalid'
    if not isinstance(citizenship, str):
        return 'invalid'
    if not isinstance(registered, bool):
        return 'invalid'

    if age < 18:
        return 'ineligible'
    if citizenship != 'citizen':
        return 'ineligible'
    if not registered:
        return 'ineligible'

    return 'eligible'

if __name__ == '__main__':
    sample_voter: dict[str, Any] = {'age': 25, 'citizenship': 'citizen', 'registered': True}
    result: str = get_voter_eligibility(sample_voter)
    print(result)