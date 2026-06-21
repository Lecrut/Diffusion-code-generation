def categorize_animals(locomotion):
    categories = {
        'swimming': ['fish', 'turtle'],
        'flying': ['bird', 'bat'],
        'walking': ['dog', 'cat']
    }
    return categories.get(locomotion, [])

if __name__ == '__main__':
    print(categorize_animals('swimming'))
    print(categorize_animals('flying'))
    print(categorize_animals('walking'))
    print(categorize_animals('crawling'))