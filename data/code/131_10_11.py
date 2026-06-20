class DecisionTreeNode:

    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label

    def predict(self, sample):
        if self.is_leaf():
            return self.label
        if sample[self.feature] < self.threshold:
            return self.left.predict(sample)
        else:
            return self.right.predict(sample)

    def is_leaf(self):
        return self.left is None and self.right is None

def build_decision_tree(samples, labels, features=None, max_depth=100):
    if features is None:
        features = list(range(len(samples[0])))
    if len(set(labels)) == 1 or not features or max_depth <= 0:
        most_common_label = max(set(labels), key=labels.count)
        return DecisionTreeNode(label=most_common_label)
    best_feature, best_threshold = find_best_split(samples, labels, features)
    left_samples, left_labels, right_samples, right_labels = split_data(samples, labels, best_feature, best_threshold)
    left_subtree = build_decision_tree(left_samples, left_labels, features[:best_feature] + features[best_feature + 1:], max_depth - 1)
    right_subtree = build_decision_tree(right_samples, right_labels, features[:best_feature] + features[best_feature + 1:], max_depth - 1)
    return DecisionTreeNode(feature=best_feature, threshold=best_threshold, left=left_subtree, right=right_subtree)

def find_best_split(samples, labels, features):
    best_gain = -1
    best_feature = None
    best_threshold = None
    for feature in features:
        unique_values = set((sample[feature] for sample in samples))
        for threshold in unique_values:
            gain = calculate_information_gain(samples, labels, feature, threshold)
            if gain > best_gain:
                best_gain = gain
                best_feature = feature
                best_threshold = threshold
    return (best_feature, best_threshold)

def calculate_information_gain(samples, labels, feature, threshold):

    def entropy(labels):
        freqs = [labels.count(label) / len(labels) for label in set(labels)]
        return -sum((p * math.log2(p) if p > 0 else 0 for p in freqs))
    base_entropy = entropy(labels)
    left_samples, left_labels, right_samples, right_labels = split_data(samples, labels, feature, threshold)
    gain = base_entropy - (len(left_labels) / len(labels) * entropy(left_labels) + len(right_labels) / len(labels) * entropy(right_labels))
    return gain

def split_data(samples, labels, feature, threshold):
    left_samples = [sample for sample in samples if sample[feature] < threshold]
    left_labels = [labels[i] for i, sample in enumerate(samples) if sample[feature] < threshold]
    right_samples = [sample for sample in samples if sample[feature] >= threshold]
    right_labels = [labels[i] for i, sample in enumerate(samples) if sample[feature] >= threshold]
    return (left_samples, left_labels, right_samples, right_labels)
if __name__ == '__main__':
    samples = [[1.0, 2.5], [1.5, 3.6], [4.2, 1.8], [7.1, 2.9], [2.3, 3.1], [4.8, 2.2], [5.5, 3.0], [7.5, 2.8], [6.3, 2.1], [8.2, 3.3]]
    labels = ['no', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no', 'yes']
    max_depth = 5
    decision_tree = build_decision_tree(samples, labels, max_depth=max_depth)
    test_samples = [[1.2, 2.8], [6.0, 3.4], [7.8, 2.5], [4.9, 1.9]]
    predictions = [decision_tree.predict(sample) for sample in test_samples]
    print('Predictions:', predictions)