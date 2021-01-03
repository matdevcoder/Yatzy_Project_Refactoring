from src.yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_ones():
        assert Yatzy.ones(1,2,3,4,5) == 1
        assert Yatzy.ones(1,2,1,4,5) == 2
        assert Yatzy.ones(6,2,2,4,5) == 0
        assert Yatzy.ones(1,2,1,1,1) == 4
        assert Yatzy.ones(1,1,1,1,1) == 5
        assert Yatzy.ones(1,2,1,1,2) == 3


def test_twos():
        assert Yatzy.twos(1,2,3,2,6) == 4
        assert Yatzy.twos(2,2,2,2,2) == 10
        assert Yatzy.twos(3,2,2,2,5) == 6
        assert Yatzy.twos(2,2,2,2,3) == 8
        assert Yatzy.twos(4,1,2,6,3) == 2
        assert Yatzy.twos(6,3,3,4,5) == 0


def test_threes():
        assert Yatzy.threes(1,2,3,2,3) == 6
        assert Yatzy.threes(2,3,3,3,3) == 12
        assert Yatzy.threes(2,1,3,1,4) == 3
        assert Yatzy.threes(2,3,3,3,5) == 9
        assert Yatzy.threes(2,5,6,1,1) == 0
        assert Yatzy.threes(3,3,3,3,3) == 15


def test_fours():
        assert Yatzy.fours(4,4,4,5,5) == 12
        assert Yatzy.fours(4,4,5,5,5) == 8
        assert Yatzy.fours(4,5,5,3,6) == 4
        assert Yatzy.fours(4,4,5,4,4) == 16
        assert Yatzy.fours(4,4,4,4,4) == 20
        assert Yatzy.fours(1,5,3,2,6) == 0


def test_fives():
        assert Yatzy.fives(4,4,4,5,5) == 10
        assert Yatzy.fives(4,4,5,5,5) == 15
        assert Yatzy.fives(4,5,5,5,5) == 20
        assert Yatzy.fives(5,5,5,5,5) == 25
        assert Yatzy.fives(4,5,3,2,6) == 5
        assert Yatzy.fives(4,1,2,6,4) == 0


def test_sixes():
        assert Yatzy.sixes(4,4,4,5,5) == 0
        assert Yatzy.sixes(4,4,6,5,5) == 6
        assert Yatzy.sixes(6,5,6,6,5) == 18
        assert Yatzy.sixes(6,6,6,6,5) == 24
        assert Yatzy.sixes(6,6,6,6,6) == 30
        assert Yatzy.sixes(2,3,2,6,6) == 12


def test_one_pair():
        assert Yatzy.score_pair(3,4,3,5,6) == 6
        assert Yatzy.score_pair(5,3,3,3,5) == 10
        assert Yatzy.score_pair(5,3,6,6,1) == 12
        assert Yatzy.score_pair(1,3,6,1,5) == 2
        assert Yatzy.score_pair(2,2,4,6,1) == 4
        


def test_two_pair():
        assert Yatzy.two_pair(3,3,5,4,5) == 16
        assert Yatzy.two_pair(3,3,6,6,6) == 18
        assert Yatzy.two_pair(3,3,6,5,4) == 0
        assert Yatzy.two_pair(3,2,2,4,4) == 12
        assert Yatzy.two_pair(1,1,5,5,6) == 12
        assert Yatzy.two_pair(3,3,2,2,4) == 10
        assert Yatzy.two_pair(6,6,5,1,1) == 14
        assert Yatzy.two_pair(3,3,4,4,6) == 14
        assert Yatzy.two_pair(6,6,5,1,5) == 22


def test_three_of_a_kind():
        assert Yatzy.three_of_a_kind(3,3,3,4,5) == 9
        assert Yatzy.three_of_a_kind(5,3,5,4,5) == 15
        assert Yatzy.three_of_a_kind(3,3,3,3,5) == 9
        assert Yatzy.three_of_a_kind(2,3,2,2,5) == 6
        assert Yatzy.three_of_a_kind(6,3,5,6,6) == 18
        assert Yatzy.three_of_a_kind(1,1,3,1,5) == 3
        assert Yatzy.three_of_a_kind(4,1,4,1,4) == 12


def test_four_of_a_kind():
        assert Yatzy.four_of_a_kind(3,3,3,3,5) == 12
        assert Yatzy.four_of_a_kind(5,5,5,4,5) == 20
        assert Yatzy.four_of_a_kind(3,3,3,3,3) == 12
        assert Yatzy.four_of_a_kind(3,3,3,2,1) == 0
        assert Yatzy.four_of_a_kind(1,1,3,1,1) == 4
        assert Yatzy.four_of_a_kind(2,2,2,5,2) == 8
        assert Yatzy.four_of_a_kind(3,6,6,6,6) == 24
        


def test_small_straight():
        
        score = 15
        
        assert Yatzy.small_straight(1,2,3,4,5) == score
        assert Yatzy.small_straight(2,3,4,5,1) == score
        assert Yatzy.small_straight(1,2,5,4,3) == score
        assert Yatzy.small_straight(2,1,3,5,4) == score
        assert Yatzy.small_straight(5,4,3,2,1) == score
        assert Yatzy.small_straight(1,6,6,5,1) == 0


def test_large_straight():
        
        score = 20
        
        assert Yatzy.largeStraight(6,2,3,4,5) == score
        assert Yatzy.largeStraight(2,3,4,5,6) == score
        assert Yatzy.largeStraight(3,5,2,6,4) == score
        assert Yatzy.largeStraight(6,2,5,3,4) == score
        assert Yatzy.largeStraight(5,6,3,4,2) == score
        assert Yatzy.largeStraight(1,2,2,4,5) == 0


def test_full_house():
        assert Yatzy.fullHouse(6,2,2,2,6) == 18
        assert Yatzy.fullHouse(2,3,4,5,6) == 0
        assert Yatzy.fullHouse(2,2,2,5,5) == 16
        assert Yatzy.fullHouse(1,3,3,1,1) == 9
        assert Yatzy.fullHouse(6,6,5,5,6) == 28

def test_chance_score():

        assert Yatzy.chance(2,3,4,5,1) == 15
        assert Yatzy.chance(3,3,4,5,1) == 16
        assert Yatzy.chance(1,3,2,5,5) == 16
        assert Yatzy.chance(1,1,1,5,1) == 9
        assert Yatzy.chance(2,2,4,5,2) == 15
        assert Yatzy.chance(6,6,4,6,6) == 28
        assert Yatzy.chance(1,3,1,5,6) == 16


def test_yatzy_scores():
        score = 50
        
        assert Yatzy.yatzy([4,4,4,4,4]) == score
        assert Yatzy.yatzy([6,6,6,6,6]) == score
        assert Yatzy.yatzy([6,6,6,6,3]) == 0
        assert Yatzy.yatzy([1,1,1,1,1]) == score
        assert Yatzy.yatzy([2,2,2,2,2]) == score
        assert Yatzy.yatzy([3,3,3,3,3]) == score
        assert Yatzy.yatzy([5,5,5,5,5]) == score