# 0: black
# 1: white

def sns_params(c) -> dict:
    if c == 0: _c = 'black'
    elif c == 1: _c = 'white'
    return {'axes.labelcolor': _c, 'xtick.color': _c, 'ytick.color': _c}

def plt_params(c) -> dict:
    if c == 0: _c = 'k'
    elif c == 1: _c = 'w'
    return {'ytick.color' : _c, 'xtick.color' : _c, 'axes.labelcolor' : _c, 'axes.edgecolor' : _c}
