import re
def get_integer_sequences(input_text):
    raw_matches = re.finditer(r'\d+', input_text)
    digits_list = []
    for match in raw_matches:
        segment = match.group(0)
        digits_list.append(int(segment))
    return digits_list

if __name__ == '__main__':
    test_data = "x99y88z77w66v55u44t33s22r11q0"
    output = get_integer_sequences(test_data)
    print(output)