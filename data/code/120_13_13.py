class ValueComparer:
    def compare(self, item1, item2):
        return item1 == item2

if __name__ == '__main__':
    comparer = ValueComparer()
    num1 = 42
    num2 = 42
    print(f"Comparing {num1} and {num2}: {comparer.compare(num1, num2)}")
    
    str1 = "apple"
    str2 = "banana"
    print(f"Comparing '{str1}' and '{str2}': {comparer.compare(str1, str2)}")
    
    float1 = 0.1 + 0.2
    float2 = 0.3
    print(f"Comparing {float1} and {float2}: {comparer.compare(float1, float2)}")