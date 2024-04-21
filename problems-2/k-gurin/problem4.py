import sys
import unittest


def search(seq: str) -> [int]:
    with open('pi.txt', 'r') as file:
        pi = file.read().replace("\n", "")
        pi = pi[2:]

        positions = []
        index = -1

        while True:
            index = pi.find(seq, index + 1)
            if index == -1:
                break
            positions.append(index)

        return positions


class TestSearchSequence(unittest.TestCase):
    def test_search(self):
        indexes = search("123")
        self.assertEqual(len(indexes), 4185)
        self.assertEqual(indexes[0], 1923)
        self.assertEqual(indexes[1], 2937)
        self.assertEqual(indexes[2], 2975)
        indexes = search("1415")
        self.assertEqual(len(indexes), 424)
        self.assertEqual(indexes[0], 0)
        self.assertEqual(indexes[1], 6954)
        self.assertEqual(indexes[2], 29135)

    def test_search_at_last_block(self):
        indexes = search("1350")
        self.assertEqual(len(indexes), 429)
        self.assertEqual(indexes[428], 4194299)

    def test_search_big_sequence(self):
        indexes = search("17450284102701938521105559644622948954930381964428810975665933446128475648233786783")
        self.assertEqual(len(indexes), 1)
        self.assertEqual(indexes[0], 154)
        indexes = search(
            "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066")
        self.assertEqual(len(indexes), 1)
        self.assertEqual(indexes[0], 0)


if __name__ == '__main__':
    try:
        user_input = input("Enter sequence to search for: ")
        positions_indexes = search(user_input)
        print(f"Found {len(positions_indexes)} results")
        print(f"Positions: {positions_indexes[:5]}")
    except FileNotFoundError:
        sys.stderr.write("File not found")
        exit(1)
    except IOError:
        sys.stderr.write("Error while reading file")
        exit(1)
