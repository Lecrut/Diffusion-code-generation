def categorize_animals():
    animals = {
        'mammal': ['lion', 'tiger', 'elephant'],
        'bird': ['eagle', 'penguin', 'sparrow'],
        'reptile': ['snake', 'lizard', 'turtle']
    }
    return animals

if __name__ == '__main__':
    categorized_animals = categorize_animals()
    print(categorized_animals)