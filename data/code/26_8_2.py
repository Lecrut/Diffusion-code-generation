import datetime

def is_voting_eligible(text: str) -> bool:
    start_index = text.find('born')
    if start_index == -1:
        return False
    start_index += 4
    year_str = text[start_index:].strip()
    if not year_str.isdigit():
        return False
    birth_year = int(year_str)
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    return age >= 18

if __name__ == '__main__':
    text = "I was born in 2000."
    result = is_voting_eligible(text)
    print(result)