class AttributeSummer:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def compute_sum(self):
        return self.attribute1 + self.attribute2

if __name__ == '__main__':
    sample_attr1 = 20
    sample_attr2 = 30
    summer_instance = AttributeSummer(sample_attr1, sample_attr2)
    total_sum = summer_instance.compute_sum()
    print(total_sum)