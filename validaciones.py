{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPxLWb6elb9vPulfX+1WMQo",
      "include_colab_link": True
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
        "<a href=\"https://colab.research.google.com/github/maximosquer76/gestion_perfiles_python/blob/main/validaciones.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {
        "id": "NeJiTl7RUg6N"
      },
      "outputs": [],
      "source": [
        "# validaciones.py\n",
        "\n",
        "def validar_texto(texto):\n",
        "    \"\"\"Verifica que el campo no esté vacío.\"\"\"\n",
        "    if not texto.strip():\n",
        "        return False\n",
        "    return True\n",
        "\n",
        "def validar_edad(edad):\n",
        "    \"\"\"Verifica que la edad sea un rango coherente.\"\"\"\n",
        "    return 18 <= edad <= 100"
      ]
    }
  ]
}
