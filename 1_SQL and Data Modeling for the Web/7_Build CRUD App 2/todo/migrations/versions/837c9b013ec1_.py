"""empty message

Revision ID: 837c9b013ec1
Revises: a6a747619653
Create Date: 2022-10-15 15:26:48.660589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '837c9b013ec1'
down_revision = 'a6a747619653'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('complete', sa.Boolean(), nullable=False),
    sa.Column('list_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['todolists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_table('todolists')
    # ### end Alembic commands ###
