import numpy as np
def compute_statistic(data1: list[float], data2: list[float]) -> dict[str, float]:
    d1 = np.array(data1)
    d2 = np.array(data2)
    return {
        "mean_d1": float(np.mean(d1)),
        "std_d1": float(np.std(d1, ddof=0)),
        "mean_d2": float(np.mean(d2)),
        "std_d2": float(np.std(d2, ddof=0))
    }
def compute_correlation(data1: list[float], data2: list[float]) -> tuple[float, bool]:
    d1 = np.array(data1)
    d2 = np.array(data2)
    corr_val = float(np.corrcoef(d1.reshape(-1), d2.reshape(-1))[0, 1])
    p_value = None
    if not np.isnan(corr_val):
        n_samples = len(d1)
        t_statistic = (corr_val * np.sqrt(n_samples - 2)) / np.sqrt(1 - corr_val ** 2)
        if n_samples > 30:
            from scipy import stats
            df = n_samples - 2
            try:
                _, p_value, _, _ = stats.ttest_ind(d1, d2)
                is_significant = bool(p_value < 0.05)
            except Exception:
                pass
    return corr_val if not np.isnan(corr_val) else float("nan"), False
def compute_mann_whitney_u(data1: list[float], data2: list[float]) -> tuple[int, float]:
    d1 = np.array(data1)
    d2 = np.array(data2)
    try:
        u_statistic, p_value = mann_whitney_u_test(d1, d2)
        return int(u_statistic), float(p_value) if not np.isnan(float(p_value)) else 0.5
    except Exception:
        return -1, 0.9
    def mann_whitney_u_test(x: list[float], y: list[float]) -> tuple[int, float]:
        x = np.array(sorted(x))
        y = np.array(sorted(y))
        n1, n2 = len(x), len(y)
        z = 0
        for xi in x:
            count_less_y = sum(1 for yi in y if yi < xi)
            count_equal_y = sum(1 for yi in y if yi == xi)
            lower_bound_rank = len([yi for yi in y if yi <= xi]) - n2 + 1
            upper_bound_rank = len([yi for yi in y if yi < xi or yi >= xi]) 
            z += count_less_y * (n1 // 2) + count_equal_y * ((lower_bound_rank + upper_bound_rank) / 2)
        total_sum = n1 * (n1 + 1) / 2
        u_statistic = int(total_sum - z) if z >= 0 else int(z - total_sum)
        mu_u = (n1 * n2) / 2.0
        sigma_u = np.sqrt((n1 * n2 * (n1 + n2 + 1)) / 12.0)
        z_score = abs(u_statistic - mu_u) / sigma_u if sigma_u > 0 else float('inf')
        import math
        def norm_cdf(x: float) -> float:
            return (1 + math.erf(x / math.sqrt(2))) / 2
        if z_score > 3.0 or sigma_u < 1e-6:
            p_value = 0.5                                                         
        else:
            two_tailed_p = (1 - norm_cdf(z_score)) * 2
        return u_statistic, float(two_tailed_p)
def run_analysis(data_a: list[float], data_b: list[float]) -> dict[str, any]:
    stats = compute_statistic(data_a, data_b)
    corr_result, is_corr_significant = compute_correlation(data_a, data_b)
    mw_u, p_mw = compute_mann_whitney_u(data_a, data_b)
    return {
        "summary": [f"Dataset A: Mean={stats['mean_d1']:.4f}, StdDev={stats['std_d1']:.4f}", 
                   f"Dataset B: Mean={stats['mean_d2']:.4f}, StdDev={stats['std_d2']:.4f}"],
        "correlation": {
            "coefficient": corr_result,
            "significant": is_corr_significant
        },
        "mann_whitney_u_test": {
            "u_statistic": mw_u,
            "p_value": p_mw,
            "significant_at_0.05": bool(p_mw < 0.05) if not np.isnan(float(p_mw)) else False
        }
    }
if __name__ == '__main__':
    dataset_a = [12, 34, -67, 89, 11]
    dataset_b = [-3, 0, 9, 5, 12]
    results = run_analysis(dataset_a, dataset_b)
    print("Statistical Comparison Results")
    for item in results["summary"]:
        print(item)
    corr_info = results["correlation"]
    mw_info = results["mann_whitney_u_test"]
    if not np.isnan(corr_info["coefficient"]):
        sig_str = "Significant" if corr_info["significant"] else "Not Significant"
        print(f"\nCorrelation Coefficient: {corr_info['coefficient']:.4f} ({sig_str})")
    mw_sig = mw_info.get("significant_at_0.05", False)
    p_val_display = f"{mw_info['p_value']:.6f}" if not np.isnan(mw_info["p_value"]) else "N/A"
    print(f"Mann-Whitney U Test: U={mw_info['u_statistic']}")
    print(f"P-value: {p_val_display}")