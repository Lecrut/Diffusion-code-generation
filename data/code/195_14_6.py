class WordCounter:
    def __init__(self):
        self.counter = {}

    def update(self, words):
        for word in (word.lower() for word in words):
            if word in self.counter:
                self.counter[word] += 1
            else:
                self.counter[word] = 1

    def subtract(self, other):
        result = WordCounter()
        for word, count in self.counter.items():
            if word in other.counter:
                result.counter[word] = count - other.counter[word]
            else:
                result.counter[word] = count
        return result

if __name__ == '__main__':
    counter1 = WordCounter()
    counter2 = WordCounter()

    sample_list1 = ['Apple', 'banana', 'Cherry', 'apple']
    sample_list2 = ['Banana', 'cherry', 'date']

    counter1.update(sample_list1)
    counter2.update(sample_list2)

    result_counter = counter1.subtract(counter2)
    for word, count in result_counter.counter.items():
        print(f"{word}: {count}")