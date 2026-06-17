import re
def extract_favorites(logs):
    favorite_animals = {}
    pattern = r'\b(favorite|likes)\s+(?:the\s+)?(\w+)\.(?=\d)'
    for log in logs:
        matches = re.findall(pattern, log)
        if not matches:
            continue
        animal_name = matches[0][1]
        try:
            count = int(matches[-1])
            favorite_animals.setdefault(animal_name, 0)
            favorite_animals[animal_name] += count
        except ValueError:
            pass
    return favorite_animals
if __name__ == '__main__':
    sample_logs = [
        "John's favorite animal is the lion. He likes it very much.",
        "Sarah loves cats and dogs equally, so she has 2 of each.",
        "The tiger in this zoo is a rare find for many visitors."
    ]
    result = extract_favorites(sample_logs)
    print(result)