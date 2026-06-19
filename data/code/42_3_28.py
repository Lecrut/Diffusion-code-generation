def build_string(elements):
    result = ""
    for element in elements:
        if result:
            result += " "
        result += str(element)
    return result

if __name__ == '__main__':
    sample_values = ['Hello', 'world', 'this', 'is', 'a', 'test']
    print(build_string(sample_values))