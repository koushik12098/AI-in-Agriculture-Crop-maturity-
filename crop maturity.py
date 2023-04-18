# Set the expected duration of growth and maturity indicators for each crop
crop_info = {
    "corn": {
        "expected_duration": 90,
        "maturity_indicator": "Are the corn kernels hard and dry? (y/n)"
    },
    "soybeans": {
        "expected_duration": 100,
        "maturity_indicator": "Are the soybean pods yellow and the leaves falling off? (y/n)"
    },
    "wheat": {
        "expected_duration": 120,
        "maturity_indicator": "Is the wheat turning golden brown and the stems are brittle? (y/n)"
    },
    "rice": {
        "expected_duration": 120,
        "maturity_indicator": "Are the rice kernels hard and the leaves turning yellow? (y/n)"
    },
    "cotton": {
        "expected_duration": 150,
        "maturity_indicator": "Are the cotton bolls open and fluffy? (y/n)"
    }
}

# Prompt the user to select a crop
crop = input(f"Select a crop to check maturity ({', '.join(crop_info.keys())}): ")

# Check if the selected crop is valid
if crop not in crop_info:
    print("Invalid crop selection.")
else:
    # Get the expected duration and maturity indicator for the selected crop
    expected_duration = crop_info[crop]["expected_duration"]
    maturity_indicator = crop_info[crop]["maturity_indicator"]

    # Prompt the user to enter the number of days the crop has grown
    days_grown = int(input("Enter the number of days the crop has grown: "))

    # Check if the crop is already mature
    if input(maturity_indicator) == "y":
        print(f"The {crop} crop is mature and ready to be harvested.")
    else:
        # Determine how many more days the crop needs to grow
        remaining_days = expected_duration - days_grown
        if remaining_days > 0:
            print(f"The {crop} crop needs to grow for {remaining_days} more days to reach maturity.")
        else:
            print(f"The {crop} crop has already exceeded the expected duration of growth.")
            print("Please seek expert advice.")
        # Exit the program after displaying the number of remaining days for the crop to mature
        exit()
