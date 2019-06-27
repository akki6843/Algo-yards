
def gaussian_function(mean,variance,variable):
     return 1.0 / sqrt(2.0 * pi *variance)*exp(-0.5 * (variable-mean) ** 2 / variance)
