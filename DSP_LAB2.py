{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPA+erDV5dSqmTV9Stg9Ywm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/amanchandra395/Signal-Visualizer/blob/main/DSP_LAB2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "def convolution(signal1, signal2):\n",
        "    result = np.zeros(len(signal1) + len(signal2) - 1)\n",
        "    for i in range(len(signal1)):\n",
        "        for j in range(len(signal2)):\n",
        "            result[i + j] += signal1[i] * signal2[j]\n",
        "    return result\n",
        "\n",
        "# Get user input for signal 1\n",
        "s1 = list(map(float, input(\"Enter signal 1, separated by spaces: \").split()))\n",
        "\n",
        "# Get user input for signal 2\n",
        "s2 = list(map(float, input(\"Enter signal 2, separated by spaces: \").split()))\n",
        "\n",
        "# Use numpy's convolve function to compute the convolution\n",
        "conv_result = np.convolve(s1, s2)\n",
        "\n",
        "# Custom implementation of convolution\n",
        "conv_result_custom = convolution(s1, s2)\n",
        "\n",
        "# Print the convolution results\n",
        "print(\"Convolution result using numpy's convolve function:\")\n",
        "print(conv_result)\n",
        "\n",
        "print(\"Convolution result using custom implementation:\")\n",
        "print(conv_result_custom)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rRJbQU0mPx5J",
        "outputId": "8a2e4e1a-40b7-4e2f-d66f-12cb7b7d6f18"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter signal 1, separated by spaces: 1 2 3 4 5\n",
            "Enter signal 2, separated by spaces: 4 5 6 7 8 9\n",
            "Convolution result using numpy's convolve function:\n",
            "[  4.  13.  28.  50.  80.  95. 100.  94.  76.  45.]\n",
            "Convolution result using custom implementation:\n",
            "[  4.  13.  28.  50.  80.  95. 100.  94.  76.  45.]\n"
          ]
        }
      ]
    }
  ]
}