from datetime import time
import pandas as pd

CITY_DATA = {'chicago': 'chicago.c  sv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid

    city_options = ['chicago', 'new york city', 'washington']

    city = None

    while city is None:
        city = str(input('Select a city to analyze: chicago, new york city, or washington:'))
        if city in city_options:
            print('You have chosen to review bike share data on %s.' % city)
        else:
            print('That is not a valid response. Please select either %s' % ', '.join(city_options))
            city = None

    month = ""
    while month != "month":
        month = str(input('Choose a month betweeh january and june to analyze or choose None.'))
        if month == "none":
            print('You have decided not to select a month.')
        elif month == "janaury, february, march, april, may, june":
            print('You have selected', month, '.')
        else:
            print('That is not a valid response. Please select either none or january, february,...,june.')

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    weekday = " "
    while weekday != "month":
        weekday = str(input('Choose a day of the week to review: monday, tuesday, wednesday,...,sunday.'))
        if weekday == "monday":
            print('You have selected Monday.')
        elif weekday == "tuesday":
            print('You have selected Tuesday.')
        elif weekday == "wednesday":
            print('You have selected Wednesday.')
        elif weekday == "thursday":
            print('You have selected Thursday.')
        elif weekday == "friday":
            print('You  have selected Friday.')
        elif weekday == "saturday":
            print('You have selected Saturday.')
        elif weekday == "sunday":
            print('You have selected Sunday.')
        else:
            print('That is not a valid response. Please select all, monday, tuesday, wednesday,...,sunday.')

        print('-' * 40)

    return city, month, weekday


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    df['Start Time'] == pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most common or popular month:', common_month)

    # TO DO: display the most common day of week
    df['Start Time'] == pd.to_datetime(df['Start Time'])
    df['date'] = df['Start Time'].dt.date
    day_of_week = df['month'].mode()[0]
    print('The most common or popular day of the week:', day_of_week)

    # TO DO: display the most common start hour
    df['Start Time'] == pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common or popular hour of the day:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    df['Start Station'] == pd.to_datetime(df['Start Time'])
    df['date'] = df['Start Time'].dt.date
    day_of_week = df['month'].mode()[0]
    print('The most common or popular day of the week:', day_of_week)

    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    with open("file.csv") as fin:
        headerline = fin.next()
        total = 0
        for row in csv.reader(fin):
            total += int(row[2])
        print(total)

        # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print('The number of users by type:', user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print('The number of users by gender:', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    # earliest is the lowest, most recent is the highest and most commor is the mode
    youngest_user = df['Birth Year'].min()
    print('The youngest user is:', youngest_user)
    oldest_user = df['Birth Year'].max()
    print('The oldest user is:', oldest_user)
    popular_year = df['Birth Year'].mode()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
