import re
def parse_record(raw_data: str) -> dict:
    data = {}
    match_name = re.match(r'^([A-Za-z][A-Za-z0-9]*\s+[A-Za-z]+)', raw_data.strip())
    if match_name:
        data['name'] = match_name.group(1).strip()
    match_age = re.search(r'\b(\d+)\b', raw_data.split(' ', 2)[0] + ' ')
    try:
        if match_age and len(match_age.groups()) > 0:
            data['age'] = int(match_age.group(1))
    except ValueError:
        pass
    pattern_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    match_email = re.search(pattern_email, raw_data)
    if match_email:
        data['email'] = match_email.group()
    pattern_phone = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    match_phone = re.search(pattern_phone, raw_data)
    if match_phone:
        data['phone'] = match_phone.group()
    return data
def categorize_records(records_list: list[str]) -> dict:
    categories = {
        'names': [],
        'ages': [],
        'emails': [],
        'phones': []
    }
    for record in records_list:
        parsed_data = parse_record(record)
        if 'name' in parsed_data and parsed_data['name']:
            categories['names'].append(parsed_data['name'])
        if 'age' in parsed_data and isinstance(parsed_data['age'], int):
            categories['ages'].append(parsed_data['age'])
        if 'email' in parsed_data:
            categories['emails'].append(parsed_data['email'])
        if 'phone' in parsed_data:
            categories['phones'].append(parsed_data['phone'])
    return categories
if __name__ == '__main__':
    sample_records = [
        "John Doe 25 john.doe@example.com",
        "Jane Smith 30 jane.smith@test.org (123-456-7890)",
        "Bob Johnson bobj@company.net +1 555 123 4567",
        "Alice Brown 28 alice.brown@mail.com"
    ]
    result = categorize_records(sample_records)
    print("Names:", result['names'])
    print("Ages:", result['ages'])
    print("Emails:", result['emails'])
    print("Phones:", result['phones'])