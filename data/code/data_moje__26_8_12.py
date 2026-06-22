import datetime

def check_voting_eligibility(text: str) -> bool:
    now = datetime.datetime.now()
    current_year = now.year
    start_index = text.find('19')
    if start_index == -1:
        return False
    year_str = text[start_index:start_index + 4]
    if len(year_str) < 4:
        return False
    try:
        birth_year = int(year_str)
    except ValueError:
        return False
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    sample_text = "Born in 1990"
    result = check_voting_eligibility(sample_text)
    print(result)