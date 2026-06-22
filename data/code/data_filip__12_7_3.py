def clean_and_verify_integers(s):
    trans_table = str.maketrans('', '', ''.join(chr(i) for i in range(256) if not chr(i).isdigit()))
    cleaned = s.translate(trans_table)
    if not cleaned:
        return False
    return cleaned.isdigit()

if __name__ == '__main__':
    sample_values = ['12345', '12a45', '  987  ', '@#$%', '123\n456', '']
    for val in sample_values:
        print(clean_and_verify_integers(val))