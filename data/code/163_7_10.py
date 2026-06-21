import csv

class FruitColorSerializer:
    HEADER = ["Fruit", "Color"]
    
    @staticmethod
    def serialize(fruits, colors, output_path):
        with open(output_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FruitColorSerializer.HEADER)
            for fruit, color in zip(fruits, colors):
                writer.writerow([fruit, color])

if __name__ == '__main__':
    fruits_list = ["apple", "banana", "cherry", "date"]
    colors_list = ["red", "yellow", "red", "brown"]
    serializer = FruitColorSerializer()
    serializer.serialize(fruits_list, colors_list, 'output.csv')