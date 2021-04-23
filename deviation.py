"""
deviation.py

Analyzes an array of measurements to get the mean value, the standard deviation,
and the standard deviation of the mean value

* Change the measurements in the main function to generate a different outcome

This file can also be imported as a module and contains the following functions:

    * calculate_mean - Calculates the mean value of a given array
    * calculate_deviation - Calculates the standard deviation of a given array
    * calculate_mean_deviation - Calculates the standard deviation of the mean value
"""

import matplotlib.pyplot as plt

import numpy as np


def calculate_mean(measurements):
    """
    Calculates the mean value of an array of measurement data

    Parameters
    ----------
    measurements : float[]
        The array of measurements

    Returns
    -------
    float
        The mean value of the given measurements
    """

    measurements_sum = 0

    for measurement in measurements:
        measurements_sum += measurement

    return measurements_sum / len(measurements)


def calculate_deviation(measurements, mean):
    """
    Calculates the standard deviation of an array of measurement data

    Parameters
    ----------
    measurements : float[]
        The array of measurements
    mean : float
        The mean value of the measurements

    Returns
    -------
    float
        The standard deviation of the given measurements
    """

    deviation_sum = 0

    for measurement in measurements:
        deviation_sum += np.square(measurement - mean)

    return np.sqrt((1 / (len(measurements) - 1)) * deviation_sum)


def calculate_mean_deviation(deviation, measurements_count):
    """
    Calculates the standard deviation of the mean value

    Parameters
    ----------
    deviation : float
        The standard deviation
    measurements_count : int
        The quantity of measurements

    Returns
    -------
    float
        The standard deviation of the mean value
    """

    return deviation / np.sqrt(measurements_count)


def plot_histogram(measurements):

    plt.figure(figsize=(12, 10), dpi=80)
    plt.grid(axis='y', alpha=0.75)

    plt.xlabel('Measured value')
    plt.ylabel('Frequency')

    plt.title('Distribution of the measurements')

    data = measurements

    n, bins, patches = plt.hist(data, bins=len(data) + 4, color='skyblue', alpha=0.7, rwidth=0.95)

    max_frequency = n.max()
    plt.ylim(ymax=np.ceil(max_frequency / 10) * 3 if max_frequency % 10 else max_frequency + 10)

    plt.show()


def main():
    """
    Main function.

    Called on script execution
    """

    print("Mean and standard deviation of measurements\n")

    measurements = [1.24, 1.2, 1.23, 1.17, 1.15, 1.26, 1.2, 1.23, 1.16, 1.17]
    print("We have the following measurements: " + str(measurements) + "\n")

    mean = calculate_mean(measurements)
    deviation = calculate_deviation(measurements, mean)
    mean_deviation = calculate_mean_deviation(deviation, len(measurements))

    print("Mean of all measurements: " + str(mean))
    print("Standard deviation of all measurements: " + str(deviation))
    print("Standard deviation of the mean of all measurements: " + str(mean_deviation))

    plot_histogram(measurements)


if __name__ == "__main__":
    main()
