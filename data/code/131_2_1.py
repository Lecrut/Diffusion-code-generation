class DecisionMaker:
    def evaluate(self, data, rules):
        decision = "No decision found"
        for rule in rules:
            if rule['condition'] == data:
                decision = rule['outcome']
                break
        return decision
if __name__ == '__main__':
    dm = DecisionMaker()
    sample_data = "sunny"
    sample_rules = [
        {'condition': "sunny", 'outcome': "Go to the beach"},
        {'condition': "rainy", 'outcome': "Stay inside"},
        {'condition': "snowy", 'outcome': "Wear warm clothes"}
    ]
    result = dm.evaluate(sample_data, sample_rules)
    print(result)