def categorize_animals():
    animals = {
        'lion': 'mammal',
        'eagle': 'bird',
        'snake': 'reptile',
        'tiger': 'mammal',
        'penguin': 'bird',
        'crocodile': 'reptile'
    }
    return animals

if __name__ == '__main__':
    categorized_animals = categorize_animals()
    print(categorized_animals)