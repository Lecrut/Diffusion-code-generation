def pair_fruits_with_colors(fruit_list):
    fruit_colors = {'apple': 'red', 'banana': 'yellow', 'grape': 'purple'}
    return [(fruit, fruit_colors.get(fruit, 'unknown')) for fruit in fruit_list]
if __name__ == '__main__':
    sample_fruits = ['apple', 'banana', 'grape', 'orange']
    print(pair_fruits_with_colors(sample_fruits))