from enalp_cli import __version__
from enalp_cli.enalp_cli import main
from click.testing import CliRunner


def test_version():
    assert __version__ == '0.1.0'


def test_tokens_word():
	runner = CliRunner()
	result = runner.invoke(main,['tokens','Hello world'])
	assert "['Hello', 'world']" in result.output
	assert result.exit_code == 0


def test_tokens_sentence():
	runner = CliRunner()
	result = runner.invoke(main,['tokens','--tokentype','sentence',"Hello word. I'm John"])
	assert '[Sentence("Hello word.")' in result.output
	assert result.exit_code == 0


def test_sentiment():
	runner = CliRunner()
	result = runner.invoke(main,['sentiment',"This movie is wonderful"])
	assert 'Sentiment(polarity=1.0, subjectivity=1.0)' in result.output
	assert result.exit_code == 0


def test_pos():
	runner = CliRunner()
	result = runner.invoke(main,['pos',"Hello, my name is Ros"])
	assert "[('Hello', 'NNP'), ('my', 'PRP$')" in result.output
	assert result.exit_code == 0


def test_readfile():
	runner = CliRunner()
	result = runner.invoke(main,['readfile','./enalp_cli/sample.txt'])
	assert "Word Tokens: ['the', 'movie', 'was', 'great']" in result.output
	assert result.exit_code == 0


def test_posdictionary():
	runner = CliRunner()
	result = runner.invoke(main,['posdictionary'])
	assert "CD	 cardinal digit" in result.output
	assert result.exit_code == 0


def test_about():
	runner = CliRunner()
	result = runner.invoke(main,['about'])
	assert "ENALP CLI: Easy NAtural Language Processing CLI" in result.output
	assert result.exit_code == 0


def test_leet():
	runner = CliRunner()
	result = runner.invoke(main,['leet','Hello Word!'])
	assert "Leet Version: #3110" in result.output
	assert result.exit_code == 0


def test_reverse():
	runner = CliRunner()
	result = runner.invoke(main,['reverse',"Hello Word!"])
	assert "Reverse Version:" in result.output
	assert result.exit_code == 0


def test_mixup():
	runner = CliRunner()
	result = runner.invoke(main,['mixup','Hello Word!'])
	assert "MixUp Version:" in result.output
	assert result.exit_code == 0


def test_plural():
	runner = CliRunner()
	result = runner.invoke(main,['plural','watch child'])
	assert "['watches', 'children']" in result.output
	assert result.exit_code == 0


def test_correction():
	runner = CliRunner()
	result = runner.invoke(main,['correction','I havv a gooda spelling'])
	assert "I have a good spelling" in result.output
	assert result.exit_code == 0


def test_definition():
	runner = CliRunner()
	result = runner.invoke(main,['definition','home'])
	assert "['where you live at a particular time'" in result.output
	assert result.exit_code == 0


def test_spell_check():
	runner = CliRunner()
	result = runner.invoke(main,['spell-check','humman'])
	assert "('human', 1.0)" in result.output
	assert result.exit_code == 0


def test_word_count():
	runner = CliRunner()
	result = runner.invoke(main,['word-count','--word_to_search','PYthoN','PYTHON Python python'])
	assert "cointains 3 time(s) the word" in result.output
	assert result.exit_code == 0


def test_translation():
	runner = CliRunner()
	result = runner.invoke(main,['translation','Buongiorno, oggi è una bella giornata'])
	assert "Good morning, today is a beautiful" in result.output
	assert result.exit_code == 0


def test_ldetect():
	runner = CliRunner()
	result = runner.invoke(main,['ldetect','Buongiorno, oggi è una bella giornata'])
	assert "The language in the Text is it" in result.output
	assert result.exit_code == 0


def test_lemmatize():
	runner = CliRunner()
	result = runner.invoke(main,['lemmatize','We watched octopi and played cards'])
	assert "'We', 'watch', 'octopus', 'and', 'play', 'card'" in result.output
	assert result.exit_code == 0
