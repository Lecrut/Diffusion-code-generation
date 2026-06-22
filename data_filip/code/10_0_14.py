class SentenceReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

    def get_original(self):
        return self.text

def reverse_sentence(sentence):
    reverser = SentenceReverser(sentence)
    return reverser.reverse_words()

if __name__ == '__main__':
    sample1 = "Python is awesome and simple"
    sample2 = "Hello World"
    sample3 = "Coding is fun"

    obj = SentenceReverser(sample1)
    print(obj.reverse_words())
    print(obj.get_original())

    obj2 = SentenceReverser(sample2)
    print(obj2.reverse_words())

    obj3 = SentenceReverser(sample3)
    print(obj3.reverse_words())

    print(reverse_sentence("Functional programming rocks"))
    print(reverse_sentence("Data science is powerful"))