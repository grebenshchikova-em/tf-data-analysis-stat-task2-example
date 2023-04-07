import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 586404828 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    start = 0.011
#    loc = x.mean()
#    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return x.mean() - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2 - start) / np.sqrt(len(x)), \
           x.mean() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))
