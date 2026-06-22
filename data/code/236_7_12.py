class Rectangle:
    WIDTH = 10
    HEIGHT = 20

    @staticmethod
    def create_instances():
        return [Rectangle() for _ in range(5)]

if __name__ == '__main__':
    instances = Rectangle.create_instances()
    print(f"Number of instances created: {len(instances)}")