import numpy as np
import pandas as pd
from parameters import generate_growth_rates, generate_interactions, generate_starting_abundances, adjust_selfinteractions
from simulations_simple_gLV import only_viable_simple_gLV, simple_gLV_with_extinction, test_simple_gLV
from graphics import abundances_line_chart, interactions_heatmap

"""Index for performing simulations based on generalized Lotka-Volterra dynamics. Calls appropriate
functions for generating interaction values, starting abundances and for generating trajectories.
To modify simulations, modify input values for functions. Standard deviation input for generating
interactions should be in the desired range, but for generating intrinsic growth rates and pairwise
interactions the standard deviation input should be as a fraction of the given mean. For example if
mean is 100 CFU and desired std is 10 CFU the input should be 0.1
"""

#Number of species
n = 40
#Maximum simulation time
maxtime = 800

ri = generate_growth_rates(n, 0.03, 0.1)

starting_abundances = generate_starting_abundances(n, 100, 0.1)

pairwise_interactions = generate_interactions(n, 1, 0, 0.004, 0.3)

pairwise_interactions = adjust_selfinteractions(n, pairwise_interactions, -0.08, 0.1)

abundances = simple_gLV_with_extinction(n, maxtime, pairwise_interactions, ri, starting_abundances)

if type(abundances) == int:
    if abundances == -1:
        print("Nonviable")
    else:
        print("Encountered error")
else:
    print(abundances[-1])
    abundances_line_chart(n, maxtime, abundances)
    #interactions_heatmap(n, pairwise_interactions)