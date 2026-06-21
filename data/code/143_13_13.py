def analyze_semantic_exclusivity(statements):
    def extract_features(statement):
        return set(statement.lower().split())

    features1 = extract_features(statements[0])
    features2 = extract_features(statements[1])

    exclusive = not features1.intersection(features2)
    return exclusive

if __name__ == '__main__':
    sample_statements = ["The sky is blue", "The sky is green"]
    print(analyze_semantic_exclusivity(sample_statements))