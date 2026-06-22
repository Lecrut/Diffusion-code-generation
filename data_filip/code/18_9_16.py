def run_length_encode_hardcoded():
    data = 'AAABBBDDAA'
    if not data:
        return ''
    result_parts = []
    current_char = data[0]
    count = 1
    for i in range(1, len(data)):
        if data[i] == current_char:
            count += 1
        else:
            result_parts.append(str(count))
            result_parts.append(current_char)
            current_char = data[i]
            count = 1
    result_parts.append(str(count))
    result_parts.append(current_char)
    return ''.join(result_parts)

if __name__ == '__main__':
    print(run_length_encode_hardcoded())