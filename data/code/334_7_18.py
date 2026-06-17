class PairDict(dict):
    def combine(self, word1: str, word2: str) -> None:
        key = (word1, word2)
        value = f"{word1}{word2}"
        super().setdefault(key, value)
def main():
    d = PairDict()
    d.combine("cat", "dog")
    d.combine("bird", "fish")
    print(d["cat", "dog"])          
    print(d["bird", "fish"])            
if __name__ == '__main__':
    main()