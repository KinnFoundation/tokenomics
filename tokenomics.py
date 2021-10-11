import scipy.integrate as integrate

def bonding_curve(n_tokens, lin_slope1 = 0.00001, lin_slope2 = 0.0001):
    # n_tokens: number of tokens 
    # returns: price of tokens
    # simple piecewise function of two lines 
    if n_tokens<1e6:
        return n_tokens*lin_slope1
    else:
        b_intercept = lin_slope1*1e6 - lin_slope2*1e6 
        return n_tokens*lin_slope2 + b_intercept


def purchase_cost(pre_token_supply, post_token_supply):
    # Calculates cost of a purchase of any quantity of tokens using the integral of the bonding curve 
    # pre_token_supply: the current total circulating supply of tokens before purchase
    # post_token_supply: the circulating token supply after purchase
    return integrate.quad(lambda x: bonding_curve(x), pre_token_supply, post_token_supply)[0]