def categorize_animals(locomotion):
    categories = {
        'swimming': ['fish', 'dolphin', 'turtle'],
        'flying': ['bird', 'bat', 'penguin'],
        'walking': ['dog', 'cat', 'horse']
    }
    return categories.get(locomotion, [])

if __name__ == '__main__':
    sample_locomotions = ['swimming', 'flying', 'walking', 'crawling']
    for locomotion in sample_locomotions:
        print(f"Animals that {locomotion}: {categorize_animals(locomotion)}")