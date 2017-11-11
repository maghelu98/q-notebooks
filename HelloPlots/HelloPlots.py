##
# Hello Plots
#

#
#  ## matplotlib
#
#  * site:      https://matplotlib.org/
#  * gallery:   https://matplotlib.org/gallery/index.html
#  * examples:  https://matplotlib.org/gallery/index.html#pyplot-examples
#

# run:
#
#  jupyter qtconsole
#  %run HelloPlots



import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['figure.figsize'] = (10,6) # (10,6), (12, 8)

def plot1() :
    '''

    '''
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

def main():
    plot1()

if __name__ == "__main__":
    main()
