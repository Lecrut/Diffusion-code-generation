import json

def run_length_encode(input_string):
    if not input_string:
        return []
    
    result = []
    count = 1
    current_char = input_string[0]
    
    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            count += 1
        else:
            result.append({
                "character": current_char,
                "count": count
            })
            current_char = input_string[i]
            count = 1
    
    result.append({
        "character": current_char,
        "count": count
    })
    
    return result

def format_rle_json(encoded_data):
    output = []
    for item in encoded_data:
        output.append(f"{item['count']}{item['character']}")
    return "".join(output)

if __name__ == '__main__':
    input_str = "AAAABBBCCDAA"
    encoded = run_length_encode(input_str)
    formatted = format_rle_json(encoded)
    output_json = json.dumps({
        "encoded_list": encoded,
        "compressed_string": formatted
    })
    print(output_json)